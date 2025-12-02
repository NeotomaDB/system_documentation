# Cloud Infrastructure

Neotoma runs as a set of components using cloud infrastructure. Neotoma's transition to the cloud occurred as a result of an NSF Grant through the CloudBank program, providing direct project funding for cloud compute resources. Through this grant we were able to deploy Neotoma as a secure cloud-available database, with multiple services, including the API, landing pages, backup and file storage and web domain management.

## System Architecture Overview

```mermaid
---
config:
  theme: neutral
  layout: elk
---

flowchart LR

%% Neotoma API Deployment
%% %% Main Branch
api_main_branch --commit--> GHA_api_main
GHA_api_main --build--> neoapi-prod-docker 
GHA_api_main --create--> neoapi-prod
neoapi-prod-docker --deploy--> neoapi-prod
neoapi-prod --> api_web
neoapi-prod -->SecurityGroup--> neotoma
neotoma --> neoapi-prod

%% %% Development Branch
api_dev_branch --commit--> GHA_api_dev
GHA_api_dev --build--> neoapi-dev-docker
GHA_api_dev --create--> neoapi-dev
neoapi-dev-docker --deploy--> neoapi-dev
neoapi-dev --> api_dev_web
neoapi-dev -->SecurityGroup--> neotomatank
neotomatank --> neoapi-dev

%% Tilia API Deployment
%% %% Main Branch
tilia_main_branch --commit--> GHA_tilia_main
GHA_tilia_main --build--> neotilia-tdev-docker
GHA_tilia_main --create--> tilia-prod
neotilia-tprod-docker --deploy--> tilia-prod
tilia-prod --> tilia_web

%% %% Development Branch
tilia_dev_branch --build--> GHA_tilia_dev
GHA_tilia_dev --build--> neotilia-tprod-docker
GHA_tilia_dev --create--> tilia-dev
neotilia-tdev-docker --deploy--> tilia-dev
tilia-dev --> tilia_dev_web

%% Static Pages
explorer_web --> Explorer
data_web --> LandingPages

%% Human Action
Administrator--SSH-->SSHIngress
SSHIngress--port-->JumpServer
JumpServer-->rdsDatabase
User --> api_web
User --> tilia_web
User --> explorer_web
User --> data_web

subgraph GitHub
    subgraph api_nodetest
        api_dev_branch[develop]
        api_main_branch[production]
    end
    subgraph tilia_api
        tilia_main_branch[production]
        tilia_dev_branch[development]
    end
    GHA_api_dev((Action))
    GHA_api_main((Action))
    GHA_tilia_dev((Action))
    GHA_tilia_main((Action))
end
subgraph AWSCloud
    subgraph S3
        LandingPages
        Explorer
    end
    subgraph VPC
        subgraph publicSubnet
            subgraph Route53
                subgraph core-api
                    api_web[api.neotomadb.org]
                    api_dev_web[api-dev.neotomadb.org]
                end
                subgraph tilia-api
                    tilia_web[tilia.neotomadb.org]
                    tilia_dev_web[tilia-dev.neotomadb.org]
                end
                data_web[data.neotomadb.org]
                explorer_web[apps.neotomadb.org]
            end
            SSHIngress
        end
        subgraph privateSubnet
            subgraph rdsDatabase
                neotoma[(neotoma)]
                neotomatank[(neotomatank)]
            end
        end
        subgraph SecurityGroups
            SecurityGroup
            JumpServer
        end
    end
    subgraph AppRunner
        neoapi-prod
        neoapi-dev
        tilia-prod
        tilia-dev
    end
    subgraph ECR
        neotilia-tprod-docker
        neotilia-tdev-docker
        neoapi-prod-docker
        neoapi-dev-docker
    end
end

Administrator[/Admin\]
User[/User\]

click api_main_branch "https:/github.com/NeotomaDB/api_nodetest" "Link to the Neotoma API Code Repository"
click tilia_main_branch "https:/github.com/NeotomaDB/tilia_api" "Link to the Tilia API Code Repository"

click api_dev_branch "https:/github.com/NeotomaDB/api_nodetest" "Link to the Neotoma API Code Repository"
click tilia_dev_branch "https:/github.com/NeotomaDB/tilia_api" "Link to the Tilia API Code Repository"

click GHA_api_dev "https://github.com/NeotomaDB/api_nodetest/blob/develop/.github/workflows/deploy.yml" "GitHub Action YAML"
click GHA_api_main "https://github.com/NeotomaDB/api_nodetest/blob/production/.github/workflows/deploy.yml" "GitHub Action YAML"

click api_web "https://api.neotomadb.org" "Neotoma API"
click api_dev_web "https://api-dev.neotomadb.org" "Neotoma Dev API"

click tilia_web "https://tilia.neotomadb.org" "Tilia API"
click tilia_dev_web "https://tiliatank.neotomadb.org" "Tilia Dev API"
```

## Core Architecture Components

### Github Repositories

The [Neotoma Database GitHub organization](https://github.com/NeotomaDB) is a core component of the database's architecture. All tools and infrastructure for Neotoma are managed through GitHub with the exception of the database's data definition file and data content.

Individual code repositories are linked to external services through [Github Actions](https://docs.github.com/en/actions/get-started/understand-github-actions), which control the way in which repositories are built and then deployed, as well as AWS CloudFormation infrastructure files that define the AWS services that are linked together to serve the applications.

Neotoma Actions are all contained in a `.github/workflows/deploy.yaml` file within individual repositories. These files define individual steps that are taken when a branch of the repository is pushed (or when periodic actions take place). The files may make use of environment variables or GitHub Secrets, such as passwords, user names, network addresses and other critical information.

### AWS Infrastructure

AWS Infrastructure consists of several key elements:

* **S3 Storage**: For database snapshots, large file storage, and delivery of "static" websites
* **Electronic Container Registry (ECR)**: For Docker containers of key software products (APIs, Python services)
* **Relational Database Service (RDS)**: For the main Neotoma Database, its backup services and ongoing maintenance
* **CloudWatch**: To manage log files for services and to observe web service status
* **Virtual Private Cloud (VPC)**: The virtual space where all cloud services are provided
* **Route 53**: The service to route Neotoma Cloud services to various web URLS
* **CloudFront**: The service to cache and serve data for Neotoma websites to reduce load time
* **Batch**: A service for code execution in the cloud, generally for longer-running services

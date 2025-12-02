# S3 Storage

## S3 Resources

S3 is the storage we use for serving static resources (Landing Pages, Explorer) and to serve snapshots of Neotoma data.

### System Overview

The S3 services are connected to our Route53 service which connects applications and internal AWS URLs to namespaces (`neotomadb.org`). Static resources (they are compiled and then largely served through the client's own browser) include Neotoma Explorer (built with Dojo) and the Neotoma Landing pages (built with Vue.js). Remote storage of database snapshots is managed through FarGate and the Batch service.

```mermaid
---
config:
  theme: neutral
  layout: elk
---

flowchart LR

%% Neotoma application deployment
%% %% Main Branch
explorer_main_branch --commit--> GHA_apps_main
GHA_apps_main --upload--> Explorer
Explorer --served_by--> explorer_web

data_main_branch --commit--> GHA_data_main
GHA_data_main --upload--> LandingPages
LandingPages --served_by--> data_web

%% %% Dev Branch
explorer_dev_branch --commit--> GHA_apps_dev
GHA_apps_dev --upload--> ExplorerDev
ExplorerDev --served_by--> explorer_dev_web

data_dev_branch --commit--> GHA_data_dev
GHA_data_dev --upload--> LandingPagesDev
LandingPagesDev --served_by--> data_dev_web

%% Human Action
User --connects_to--> explorer_web
User --connects_to--> data_web
User --calls_to--> api_web

subgraph GitHub
    subgraph explorer
        explorer_dev_branch[develop]
        explorer_main_branch[production]
    end
    subgraph landingpages
        data_main_branch[production]
        data_dev_branch[development]
    end
    GHA_apps_dev((Action))
    GHA_apps_main((Action))
    GHA_data_dev((Action))
    GHA_data_main((Action))
end
subgraph AWSCloud
    subgraph S3
        LandingPages
        LandingPagesDev
        Explorer
        ExplorerDev
    end
    subgraph VPC
        subgraph publicSubnet
            subgraph Route53
                data_web[data.neotomadb.org]
                explorer_web[apps.neotomadb.org]
                data_dev_web[data-dev.neotomadb.org]
                explorer_dev_web[apps-dev.neotomadb.org]
                api_dev_web[api-dev.neotomadb.org]
                api_web[api.neotomadb.org]
            end
        end
    end
end

User[/User\]

click explorer_main_branch "https:/github.com/NeotomaDB/Explorer" "Link to the Neotoma Explorer Code Repository"
click explorer_dev_branch "https:/github.com/NeotomaDB/Explorer" "Link to the Neotoma Explorer Code Repository"

click data_main_branch "https:/github.com/NeotomaDB/landingpagesv3" "Link to the Neotoma Landing Pages Code Repository"
click data_dev_branch "https:/github.com/NeotomaDB/landingpagesv3" "Link to the Neotoma Landing Pages Code Repository"


click GHA_apps_main "https://github.com/NeotomaDB/Explorer/blob/main/.github/workflows/deploy.yml" "GitHub Action YAML"
click GHA_data_main "https://github.com/NeotomaDB/landingpagesv3/blob/production/.github/workflows/deploy.yml" "GitHub Action YAML"
click GHA_data_dev "https://github.com/NeotomaDB/landingpagesv3/blob/production/.github/workflows/deploy.yml" "GitHub Action YAML"

click explorer_web "https://apps.neotomadb.org" "Neotoma Apps Service"
click data_web "https://data.neotomadb.org" "Neotoma Landing Pages"
click data_dev_web "https://data-dev.neotomadb.org" "Neotoma Landing Pages Dev"

```

## Resources


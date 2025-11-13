# API Documentation

The Research Database API provides programmatic access to the database through RESTful endpoints.

## Interactive API Documentation

<swagger-ui src="openapi.yaml"/>

## Quick Links

- [Authentication Guide](authentication.md)
- [Quick Start](quickstart.md)
- [Endpoints by Database Table](endpoints/by-table.md)

## Base URL

**Production**: `https://api.neotomadb.org/`  
**Development**: `http://api-dev.neotomadb.org`

## Authentication

All API requests require authentication. See the [Authentication Guide](authentication.md) for details.

## Rate Limits

- **Authenticated requests**: 1000 requests/hour
- **Unauthenticated requests**: 100 requests/hour

## Support

For API support, contact: [goring@wisc.edu](mailto:goring@wisc.edu)

---

*API Version: {{ api_version() }} | Last Updated: {{ last_validated() }}*

---
title: References - API
sidebar_position: 0
image: og/docs/api.jpg
# tags: ['schema']
---
import Badges from '/_includes/badges.mdx';

<Badges/>

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
# Introduction

A data schema is the first thing you can define, before you can start adding data. Designing and adding a data schema is not a requirement; if you don't add a data schema, an automatic schema will be generated from the data that you import (available from Weaviate version v1.5.0). A data schema specifies what data classes your Weaviate will have, and what properties data objects consist of. Per the data class property, you will define what data type its value can adopt. If you want to make graph links between data objects, you'll also define that in the data type of class properties.

Additionally, per the data class, you can define the vector index type, the vectorizer module and, optionally, other modules. Specific settings to modules and the vector index type can also be set per class and per property. 

Learn more about 
1. [Configuration](./schema-configuration.md) of the classes and properties in the schema.
2. [Data types](./datatypes.md) of property values.
3. [Schema endpoint](../references/rest/schema.md).
4. [Auto-schema](./schema-configuration.md#auto-schema), for more information about settings for the auto generated schema.

A Weaviate data schema is slightly different from a taxonomy, which has a hierarchy. Read more about how taxonomies, ontologies and schemas are related to Weaviate in [this blog post](https://medium.com/semi-technologies/taxonomies-ontologies-and-schemas-how-do-they-relate-to-weaviate-9f76739fc695).

<<<<<<< HEAD
> 💡 Check out the [schema getting started guide](/docs/weaviate/getting-started/schema.md) to learn how to work with the Weaviate schema in under 10 minutes.

=======
=======
<!-- TODO: Refine layout for presentation -->
:::caution Migrated From:
=======
<!-- :::caution Migrated From:
>>>>>>> 6a0ac70 (Comment out notes re correlation to old site)
- `GraphQL`
- `RESTful API`
::: -->

<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 297889f (Added explanatory boxes for provenance; lots of minor edits)
## References - GraphQL
=======
=======
:::info Related pages
- [Concepts: Interface](../concepts/interface.md)
:::

>>>>>>> 4078f10 (Added xrefs)
## Overview

This section includes references for the RESTful and GraphQL APIs. The RESTful API end-points can be used to add data and the GraphQL interface to retrieve data.

### References - GraphQL
>>>>>>> e10d7a4 (Updated Overview pages)
- [Get{}](./graphql/get.md)
- [Aggregate{}](./graphql/aggregate.md)
- [Explore{}](./graphql/explore.md)
- [Filters](./graphql/filters.md)
- [Vector search parameters](./graphql/vector-search-parameters.md)
- [Additional properties](./graphql/additional-properties.md)

### References - RESTful API
- [Overview](./rest/index.md)
- [/v1/schema](./rest/schema.md)
- [/v1/objects](./rest/objects.md)
- [/v1/batch](./rest/batch.md)
- [/v1/backups](./rest/backups.md)
- [/v1/classification](./rest/classification.md)
- [/v1/meta](./rest/meta.md)
- [/v1/nodes](./rest/nodes.md)
- [/v1/.well-known](./rest/well-known.md)
- [/v1/modules](./rest/modules.md)

<<<<<<< HEAD
## References - Client libraries
- [Python](./client-libraries/python.md)
- [Javascript](./client-libraries/javascript.md)
- [Java](./client-libraries/java.md)
- [Go](./client-libraries/go.md)
- [Weaviate CLI](./client-libraries/cli.md)

## References - Schema
- [Configuration](./schema-configuration.md) of the classes and properties in the schema.
- [Data types](./datatypes.md) of property values.
- [Schema endpoint](../references/rest/schema.md).
- [Auto-schema](./schema-configuration.md#auto-schema), for more information about settings for the auto generated schema.
>>>>>>> b8e2056 (updated refs section)
=======
>>>>>>> e10d7a4 (Updated Overview pages)
## More Resources
=======
:::note
Check out the [schema getting started guide](/developers/weaviate/current/getting-started/schema.html) to learn how to work with the Weaviate schema in under 10 minutes.
:::
>>>>>>> 6954b32 (updated config; minor changes to others)

import DocsMoreResources from '/_includes/more-resources-docs.md';

<DocsMoreResources />

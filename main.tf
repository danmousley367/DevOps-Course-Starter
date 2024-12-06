terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 3.8"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "d33b95c7-af3c-4247-9661-aa96d47fccc0"
}

data "azurerm_resource_group" "main" {
  name = "cohort32-33_DanMou_ProjectExercise"
}

resource "azurerm_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_linux_web_app" "main" {
  name                = "danmou-061224-terraform-todoapp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      docker_image_name   = "danmou367/my-todo-app:latest"
      docker_registry_url = "https://index.docker.io"
    }
  }

  app_settings = {
    "FLASK_APP"                   = "todo_app/app"
    "FLASK_DEBUG"                 = true
    "SECRET_KEY"                  = "secret-key"
    "COSMOS_DB_CONNECTION_STRING" = azurerm_cosmosdb_account.db.primary_mongodb_connection_string
    "OAUTH_CLIENT_ID"             = "Ov23liT1z8nNtSCOyVtN"
    "OAUTH_CLIENT_SECRET"         = "cf6aa082e19da7a22af3f3e4e616266d933cb014"
    "OAUTHLIB_INSECURE_TRANSPORT" = 1
  }
}

resource "azurerm_cosmosdb_account" "db" {
  name                = "danmou-terraform-cosmos-account"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities {
    name = "EnableServerless"
  }

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "ukwest"
    failover_priority = 0
  }
}

resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = "danmou-terraform-cosmos-mongodb"
  resource_group_name = azurerm_cosmosdb_account.db.resource_group_name
  account_name        = azurerm_cosmosdb_account.db.name

  lifecycle {
    prevent_destroy = true
  }
}
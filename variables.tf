variable "prefix" {
  description = "The prefix used for all resources in this environment"
  default = "test"
}

variable "oauth_client_id" {
  description = "Client ID for connecting to OAuth app"
  sensitive = true
}

variable "oauth_client_secret" {
  description = "Client secret for connecting to OAuth app"
  sensitive = true
}
terraform {
  backend "gcs" {
    bucket = "demo-gha"
    prefix = "resource-creation/"
  }
}

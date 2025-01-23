module "primary" {
  source = "./module"
  cluster_name     = var.cluster_name
  region = var.region
  initial_node_count = var.initial_node_count
}
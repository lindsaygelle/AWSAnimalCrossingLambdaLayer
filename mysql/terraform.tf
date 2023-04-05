terraform {
  backend "s3" {
    bucket = "385739365063"
    key    = "AWS/AnimalCrossing/LambdaLayer/mysql/terraform.tfstate"
    region = "us-east-1"
  }
}
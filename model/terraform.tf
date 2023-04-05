terraform {
  backend "s3" {
    bucket = "385739365063"
    key    = "AWS/AnimalCrossing/LambdaLayer/model/terraform.tfstate"
    region = "us-east-1"
  }
}
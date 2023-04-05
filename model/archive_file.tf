data "archive_file" "model" {
  output_path = "./AnimalCrossingModel.zip"
  source_dir  = "./src"
  type        = "zip"
}
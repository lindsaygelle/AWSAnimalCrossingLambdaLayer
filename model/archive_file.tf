data "archive_file" "main" {
  output_path = "./AnimalCrossingModel.zip"
  source_dir  = "./src"
  type        = "zip"
}
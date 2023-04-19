data "archive_file" "main" {
  output_path = "./AnimalCrossingMySql.zip"
  source_dir  = "./src"
  type        = "zip"
}
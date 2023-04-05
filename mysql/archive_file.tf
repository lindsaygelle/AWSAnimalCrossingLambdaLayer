data "archive_file" "main" {
  output_path = "./AnimalCrossingMySQL.zip"
  source_dir  = "./src"
  type        = "zip"
}
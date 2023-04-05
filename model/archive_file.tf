data "archive_file" "model" {
  output_path = "./model.zip"
  source_dir  = "./src"
  type        = "zip"
}
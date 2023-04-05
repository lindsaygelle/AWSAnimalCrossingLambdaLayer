resource "aws_lambda_layer_version" "model" {
  compatible_runtimes = ["python3.8"]
  filename            = data.archive_file.model.output_path
  layer_name          = "AnimalCrossingModel"
  source_code_hash    = filebase64sha256(data.archive_file.model.output_path)
}
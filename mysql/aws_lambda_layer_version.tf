resource "aws_lambda_layer_version" "main" {
  compatible_architectures = ["arm64", "x86_64"]
  compatible_runtimes      = ["python3.7", "python3.8", "python3.9"]
  description              = "Animal Crossing MySQL connector-python."
  filename                 = data.archive_file.main.output_path
  layer_name               = "AnimalCrossingMySQLConnectorPython"
  skip_destroy             = false
  source_code_hash         = filebase64sha256(data.archive_file.main.output_path)
}
resource "aws_lambda_layer_version" "main" {
  compatible_architectures = ["arm64", "x86_64"]
  compatible_runtimes      = ["python3.7", "python3.8", "python3.9"]
  description              = "Animal Crossing data models."
  filename                 = data.archive_file.main.output_path
  layer_name               = "AnimalCrossingModel"
  skip_destroy             = false
  source_code_hash         = filebase64sha256(data.archive_file.main.output_path)
}
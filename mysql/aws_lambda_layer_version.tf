resource "aws_lambda_layer_version" "main" {
  compatible_architectures = ["arm64", "x86_64"]
  compatible_runtimes      = ["python3.8", "python3.9"]
  description              = "https://github.com/mysql/mysql-connector-python/blob/trunk/README.rst"
  filename                 = data.archive_file.main.output_path
  layer_name               = "AnimalCrossingMySql"
  license_info             = "https://github.com/mysql/mysql-connector-python/blob/trunk/LICENSE.txt"
  skip_destroy             = false
  source_code_hash         = filebase64sha256(data.archive_file.main.output_path)
}
output "arn" {
  value = aws_lambda_layer_version.main.arn
}

output "filename" {
  value = aws_lambda_layer_version.main.filename
}

output "compatible_runtimes" {
  value = aws_lambda_layer_version.main.compatible_runtimes
}
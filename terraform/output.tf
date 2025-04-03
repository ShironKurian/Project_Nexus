output "rds_endpoint" {
  description = "PostgreSQL Database Endpoint"
  value       = aws_db_instance.postgres.endpoint
}
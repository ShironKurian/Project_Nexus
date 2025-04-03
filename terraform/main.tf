resource "aws_db_instance" "postgres" {
  engine                 = "postgres"
  engine_version         = var.db_engine_version
  instance_class         = var.db_instance_class
  allocated_storage      = var.db_allocated_storage
  db_name               = var.db_name
  username              = var.db_username
  password              = var.db_password
  parameter_group_name  = "default.postgres15"
  publicly_accessible   = true
  skip_final_snapshot   = true
}
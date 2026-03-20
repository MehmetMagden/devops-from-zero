import click
import boto3
from moto import mock_aws


def add(x,y):
    return x+y

@mock_aws  # ← Bu satır AWS'i taklit eder, gerçek hesap gerekmez!
def create_fake_buckets():
    """Test için sahte bucket'lar oluştur"""
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="mehmet-bucket-1")
    s3.create_bucket(Bucket="mehmet-bucket-2")
    s3.create_bucket(Bucket="mehmet-bucket-3")
    return s3

@click.command()
@mock_aws  # ← Burada da taklit et
def buckets():
    """Bu komut bucket'ları listeler"""
    s3 = create_fake_buckets()
    all_buckets = s3.list_buckets()["Buckets"]

    click.echo(click.style("=== S3 Bucket Listesi ===", fg="green"))
    for bucket in all_buckets:
        click.echo(
            click.style(f"  → {bucket['Name']}", bg="yellow", fg="blue")
        )

if __name__ == "__main__":
    buckets()

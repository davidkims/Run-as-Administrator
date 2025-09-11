#!/usr/bin/env python3
"""AWS IAM access key management script for DefenderBot.

This script allows you to list, create, and delete access keys for a
specified IAM user. Optionally, newly created keys can be stored in AWS
Secrets Manager.

Usage examples:
    python defenderbot_key_manager.py list --user exampleUser
    python defenderbot_key_manager.py create --user exampleUser --secret-name my/secret
    python defenderbot_key_manager.py delete --user exampleUser --access-key-id AKIA...
"""

import argparse
import datetime
import json

import boto3


def list_existing_keys(user_name: str):
    """Return a list of existing access keys for the user."""
    iam_client = boto3.client("iam")
    response = iam_client.list_access_keys(UserName=user_name)
    return response.get("AccessKeyMetadata", [])


def create_and_store_access_key(user_name: str, secret_name: str | None = None):
    """Create a new access key and optionally store it in Secrets Manager."""
    iam_client = boto3.client("iam")
    response = iam_client.create_access_key(UserName=user_name)
    access_key = response["AccessKey"]["AccessKeyId"]
    secret_key = response["AccessKey"]["SecretAccessKey"]

    if secret_name:
        secrets_client = boto3.client("secretsmanager")
        payload = {
            "AccessKeyId": access_key,
            "SecretAccessKey": secret_key,
            "CreatedAt": datetime.datetime.utcnow().isoformat() + "Z",
        }
        secrets_client.put_secret_value(
            SecretId=secret_name, SecretString=json.dumps(payload)
        )
    return access_key


def delete_access_key(user_name: str, access_key_id: str):
    """Delete the specified access key for the user."""
    iam_client = boto3.client("iam")
    iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List existing access keys")
    list_parser.add_argument("--user", required=True, help="IAM user name")

    create_parser = subparsers.add_parser("create", help="Create a new access key")
    create_parser.add_argument("--user", required=True, help="IAM user name")
    create_parser.add_argument(
        "--secret-name", help="Optional Secrets Manager secret name"
    )

    delete_parser = subparsers.add_parser("delete", help="Delete an access key")
    delete_parser.add_argument("--user", required=True, help="IAM user name")
    delete_parser.add_argument(
        "--access-key-id", required=True, help="Access key ID to delete"
    )

    args = parser.parse_args()

    if args.command == "list":
        keys = list_existing_keys(args.user)
        for key in keys:
            print(f"{key['AccessKeyId']}\t{key['Status']}")
    elif args.command == "create":
        new_key = create_and_store_access_key(args.user, args.secret_name)
        print(f"Created new access key: {new_key}")
    elif args.command == "delete":
        delete_access_key(args.user, args.access_key_id)
        print(f"Deleted access key: {args.access_key_id}")


if __name__ == "__main__":
    main()

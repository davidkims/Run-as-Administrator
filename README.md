# Run-as-Administrator

Utility scripts and examples.

## AWS Access Key Management

`defenderbot_key_manager.py` provides a small command line interface for
listing, creating and deleting AWS IAM access keys for a given user.  When
creating a key, the script can optionally store the credentials in AWS
Secrets Manager.

### Usage

```
python defenderbot_key_manager.py list --user exampleUser
python defenderbot_key_manager.py create --user exampleUser --secret-name my/secret
python defenderbot_key_manager.py delete --user exampleUser --access-key-id AKIA...
```

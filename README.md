# pre-commit-k8s

An additional hook that can be used as a hook with (pre-commit)[https://pre-commit.com/] to validate Kubernetes objects.

Current hooks:

* `kubernetes-secrets` - check if secrets are pushed

## Usage

Install pre-commit

```
pip install pre-commit
```

Setup the `.pre-commit-config.yaml` config file:

```
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
- repo: https://github.com/zwennesm/pre-commit-k8s
  rev: v0.0.1
  hooks:
  - id: pre-commit-k8s
    entry: pre-commit-k8s
```

Install the pre-commit hooks:

```
pre-commit install
```

## Local install

Alternatively `pre-commit-k8s` can be installed locally for testing.

```
pip install pre-commit-k8s
```

`pre-commit-k8s` expects a list of files to be passed to it:

```
➜ pre-commit-k8s LICENCE                                          
2020-12-07 14:50:06,636 - INFO - Validating the following rules:
2020-12-07 14:50:06,636 - INFO - ✓ Kubernetes Secret check
2020-12-07 14:50:06,636 - INFO - No validation errors found
```

Rules can also be excluded:

```
➜ pre-commit-k8s --exclude kubernetes-secrets kubernetes-secret.yaml 
2020-12-07 14:52:08,569 - WARNING - No rules activated to validate files
2020-12-07 14:52:08,569 - INFO - No validation errors found
```
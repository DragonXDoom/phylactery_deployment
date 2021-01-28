# Phylactery Deployment

Deployment configuration and encrypted secrets for deploying Phylactery.

Secrets are stored in the `secrets` folder and configured to be committed using the `git-crypt` utility. You will need a valid GPG key to unlock the secrets.

## Prerequesites
- Running Traefik v2 instance to act as reverse proxy
- Make sure `git-crypt` is installed: `apt install git-crypt`

## Deployment
- `git clone --recurse-submodules` this repository and `cd` into it
  - If you cloned without submodules, you can clone them now with `git submodule update --init --recursive`
- `git-crypt unlock /path/to/keyfile` to decrypt secrets (never commit the keyfile to this repository)
- Check you are happy with `.env`
- Make folders as necessary:
  - `source .env` to load environment variables
  - `mkdir -p $DATABASE_PERSISTENT_ROOT`
- `docker-compose build` to rebuild the images for good measure
  - This may take a few minutes depending on cache
- `docker-compose up -d`

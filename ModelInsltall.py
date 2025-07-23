from huggingface_hub import snapshot_download

# Download all model weights
snapshot_download(repo_id='opendatalab/pdf-extract-kit-1.0', local_dir='./', max_workers=20)

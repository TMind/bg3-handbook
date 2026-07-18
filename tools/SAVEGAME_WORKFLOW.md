# Savegame Sync Workflow

Purpose: keep handbook audits based on the newest real BG3 save, without manually copying save files into the vault.

## Source

The original saves live on **tmind's Mac**, under his Steam userdata:

`~/Library/Application Support/Steam/userdata/13763549/1086940/remote/_SAVE_Public/Savegames/Story`

The sync tool scans that path plus the common Larian profile save folders by default.

### On Kao's machine

Kao has no BG3 saves in Steam userdata — that folder holds profile data only, no `.lsv` files — so the default scan finds nothing and the bare `sync_latest_save.py` will not work.

Kao's copies of TMind's saves live in the repo's gitignored `saves/` folder instead. It uses the same `folder/name.lsv` layout, so point the tool at it explicitly:

```sh
python3 tools/sync_latest_save.py --source-root saves --list 5
python3 tools/sync_latest_save.py --source-root saves
```

Everything downstream (extract, manifest, index) behaves the same. The limitation is upstream: `saves/` only refreshes when a new save is copied over from tmind, so Kao cannot pull fresh in-game state on his own. Every command below assumes `--source-root saves` when run on Kao's machine.

## First-Time Setup

Install the Python libraries used by the local extractor:

```sh
python3 -m pip install --target /private/tmp/bg3-py-libs -r tools/requirements-save-tools.txt
```

## Standard Procedure

1. Save the game in BG3.
2. Wait a few seconds for Steam Cloud/local file sync.
3. List the newest saves:

```sh
python3 tools/sync_latest_save.py --list 5
```

4. Sync and extract the newest save:

```sh
python3 tools/sync_latest_save.py
```

This writes:

- `tools/current-save/latest.lsv`
- `saves/<save-folder>/...`
- `tools/save-extract/*`
- `tools/save-extract/source_manifest.json`

Use `saves/` as the human-accessible mirror of selected real saves. It keeps the original save folder name and copies sibling files such as the preview `.WebP` when present. This folder is intentionally ignored by Git because save files are large binaries.

Treat `tools/save-extract` as disposable raw extract output. Do not store hand-written notes there.

## If the Newest Save Is Not the Right One

Use the index from `--list`:

```sh
python3 tools/sync_latest_save.py --index 1
```

Or filter by visible save name:

```sh
python3 tools/sync_latest_save.py --name-filter QuickSave
```

## LSF to LSX Step

The Python extractor refreshes the raw `.lsf` files. Some handbook analysis still expects the readable `Globals.lsx`.

After syncing, refresh `Globals.lsx` with LSLib/Divine if a new text export is needed:

- input: `tools/save-extract/Globals.lsf`
- output: `tools/save-extract/Globals.lsx`

Command shape:

```sh
CX_BOTTLE=Steam "/Users/tmind/Applications/CrossOver.app/Contents/SharedSupport/CrossOver/CrossOver-Hosted Application/wine" \
  tools/Packed/Tools/Divine.exe \
  -g bg3 \
  -a convert-resource \
  -s "tools/save-extract/Globals.lsf" \
  -d "tools/save-extract/Globals.lsx" \
  -i lsf \
  -o lsx
```

Inside the Codex sandbox this Wine step may fail with a `wineserver` permission error. In that case run the command in a normal macOS Terminal from the handbook folder.

Keep this as a conversion step only. Never edit or repack the save.

## Audit Rule

Every generated snapshot should cite `tools/save-extract/source_manifest.json` as the source of truth. If the manifest changed, rerun the relevant party, item, buff, and readiness audits before updating handbook recommendations.

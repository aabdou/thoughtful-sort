# Thoughtful Robot

## Install dependencies

### With uv

```bash
uv sync
```

### Without uv

```bash
pip install pytest
```

## Test

### With uv

```bash
uv run pytest test_robot.py
```

### Without uv

```bash
pytest test_robot.py
```

## To run the CLI:
```bash
python main.py --width_cm 10 --height_cm 20 --length_cm 30 --mass_kg 5
```
# NFL Public Data & Forecasting Pipeline — upgraded bundle

## Files
1. `NFL_Public_Data_Warehouse.ipynb` — public data collector, with an added post-collection file audit; exports separate datasets into `nfl_data/`.
2. `NFL_Coaching_Data_Collection_v2.ipynb` — coaching source registry, verified tenure/change schemas, and play-by-play-derived team tendencies.
3. `NFL_Analysis_and_Neural_Networks_v2.ipynb` — position trends, lagged features, position-specific models, chronological holdout metrics, walk-forward evaluation, approximate residual intervals, and next-game/rest-of-season/next-year templates.

## Run order
1. Open the warehouse notebook and run it in JupyterLab.
2. Open the coaching notebook. Keep `DATA_ROOT = Path("nfl_data")` pointed at the same directory.
3. Open the analysis notebook. It loads the exported tables from the same `nfl_data/` directory and writes outputs to `nfl_forecasts/`.

## Environment
Core recommended packages:
`pandas numpy requests pyarrow scikit-learn matplotlib joblib`

If Parquet support is unavailable, the notebooks attempt CSV fallbacks. Optional deep-learning libraries are not required for the v2 modeling workflow; an sklearn MLP neural network is included. Use a current Python environment and install missing packages with pip/conda as appropriate.

## Modeling design
- Canonical player-game table: inspect columns and verify one row per player/game.
- Position-specific models: fit only when there are enough rows and seasons.
- Models compared: training-mean baseline, Ridge, Extra Trees, HistGradientBoosting, and MLP.
- Time split: latest season is held out; a rolling-origin helper provides additional backtests.
- Prediction intervals: residual-based approximate intervals; these are not guaranteed calibrated intervals.
- Rest-of-season: simulation helper accepts future player-game predictions with uncertainty bounds. It still needs a schedule-aware forecast table.
- Next season: produces a player-season training table and documents required pre-season features; it is not a complete roster/role-transition model.

## Coaching coverage
The coaching notebook does not claim to automatically obtain a complete coach/coordinator history. It provides an auditable source registry and schemas for verified records, plus measurable play-calling proxies from play-by-play. Fill coach tenures and changes from public sources with source URLs and checked dates. Detailed scheme labels and tracking/All-22 data may be unavailable or licensed.

## Critical checks before trusting results
- Check the inventory and missing tables.
- Verify target column semantics and player-game uniqueness.
- Avoid future leakage: use only information available at the prediction cutoff.
- Do not join full-season tendencies to early-week rows.
- Compare against simple baselines; report metrics by position and season.
- Use several rolling-origin test seasons before production.
- Forecasts are estimates, not guarantees or betting advice.

## Output folders
- `nfl_data/`: raw/collected datasets and coaching subfolder.
- `nfl_forecasts/`: metrics, trend charts, model files, model card, and forecast templates.

"""
Convert Sensor Logger CSV exports into the single-file format used by the HMM notebook.

Usage:
  python convert_sensorlogger.py <folder_with_exports> <member> <activity> [--test]

<folder_with_exports> contains one sub-folder per recording (each with Accelerometer.csv
and Gyroscope.csv). Sub-folders are processed in alphabetical (= time) order.

Training output : data/train/<activity>/<member>_<activity>_NN.csv
With --test     : data/test/<member>_<activity>_NN.csv  (rename to sessionN.csv as needed)
"""
import sys, os, glob
import numpy as np, pandas as pd

def read_sensor(rec_dir, name):
    """Read <name>.csv; if it is empty/missing (common on iPhone) use <name>Uncalibrated.csv."""
    for fn in (f"{name}.csv", f"{name}Uncalibrated.csv"):
        p = os.path.join(rec_dir, fn)
        if os.path.exists(p) and os.path.getsize(p) > 0:
            return pd.read_csv(p)
    raise FileNotFoundError(f"no data for {name} in {rec_dir}")

def convert(rec_dir):
    acc = read_sensor(rec_dir, "Accelerometer")
    gyr = read_sensor(rec_dir, "Gyroscope")
    t = acc["seconds_elapsed"].values                      # use accelerometer timeline
    out = pd.DataFrame({"timestamp": t, "ax": acc["x"], "ay": acc["y"], "az": acc["z"]})
    for c in ["x", "y", "z"]:                              # align gyroscope to it
        out["g" + c] = np.interp(t, gyr["seconds_elapsed"].values, gyr[c].values)
    return out

if __name__ == "__main__":
    root, member, activity = sys.argv[1:4]
    test = "--test" in sys.argv
    out_dir = "data/test" if test else f"data/train/{activity}"
    os.makedirs(out_dir, exist_ok=True)
    folders = sorted(d for d in glob.glob(os.path.join(root, "*")) if os.path.isdir(d))
    for i, d in enumerate(folders, 1):
        try:
            df = convert(d)
        except Exception as e:
            print(f"skip {d}: {e}"); continue
        path = f"{out_dir}/{member}_{activity}_{i:02d}.csv"
        df.to_csv(path, index=False)
        print(f"{d} -> {path}  ({len(df)} rows, {len(df)/df['timestamp'].iloc[-1]:.1f} Hz)")

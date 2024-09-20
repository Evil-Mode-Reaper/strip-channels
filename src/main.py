import librosa
import numpy as np
from pathlib import Path, PurePath
import soundfile as sf


def main():
    src: str = input("Enter path to directory containing audio files to edit: ")
    src_p: Path = Path(src)
    try:
        src_pr: Path = src_p.resolve(strict=True)
    except Exception as error:
        raise error

    stripped: list[Path] = []
    N_CHAN = 10 # Only edit files with this number of channels
    for file in src_pr.iterdir():
        with sf.SoundFile(file, 'r+') as f:
            if f.channels != N_CHAN:
                print(f"Skipping {file.name}, as its channel count is not {str(N_CHAN)}.")
                continue

            audio, samplerate = librosa.load( path=file, sr=f.samplerate, mono=False)
            np.delete(audio, 0)
            np.delete(audio, 1)

            f.write(audio)
            if f.channels != (N_CHAN - 2):
                print(f"Could not strip the first two channels from {file.name}!")

            stripped.append(file)

    print("Stripped the first two channels from the following files:")
    for s in stripped:
        print(s.name)


if __name__ == "__main__":
    main()

"""Test suites for checking numerical compatibility against Kaldi"""
import torchaudio.compliance.kaldi
from parameterized import parameterized
from torchaudio_unittest.common_utils import (
    TestBaseMixin,
    TempDirMixin,
    load_params,
    skipIfNoExec,
    get_asset_path,
    load_wav,
)
from torchaudio_unittest.common_utils.kaldi_utils import (
    convert_args,
    run_kaldi,
)


class Kaldi(TempDirMixin, TestBaseMixin):
    def assert_equal(self, output, *, expected, rtol=None, atol=None):
        expected = expected.to(dtype=self.dtype, device=self.device)
        self.assertEqual(output, expected, rtol=rtol, atol=atol)

    @parameterized.expand(load_params("kaldi_test_fbank_args.jsonl"))
    @skipIfNoExec("compute-fbank-feats")
    def test_fbank(self, kwargs):
        """fbank should be numerically compatible with compute-fbank-feats"""
        wave_file = get_asset_path("kaldi_file.wav")
        waveform = load_wav(wave_file, normalize=False)[0].to(dtype=self.dtype, device=self.device)
        result = torchaudio.compliance.kaldi.fbank(waveform, **kwargs)
        command = ["compute-fbank-feats"] + convert_args(**kwargs) + ["scp:-", "ark:-"]
        kaldi_result = run_kaldi(command, "scp", wave_file)
        self.assert_equal(result, expected=kaldi_result, rtol=1e-4, atol=1e-8)

    @parameterized.expand(load_params("kaldi_test_spectrogram_args.jsonl"))
    @skipIfNoExec("compute-spectrogram-feats")
    def test_spectrogram(self, kwargs):
        """spectrogram should be numerically compatible with compute-spectrogram-feats"""
        wave_file = get_asset_path("kaldi_file.wav")
        waveform = load_wav(wave_file, normalize=False)[0].to(dtype=self.dtype, device=self.device)
        result = torchaudio.compliance.kaldi.spectrogram(waveform, **kwargs)
        command = ["compute-spectrogram-feats"] + convert_args(**kwargs) + ["scp:-", "ark:-"]
        kaldi_result = run_kaldi(command, "scp", wave_file)
        self.assert_equal(result, expected=kaldi_result, rtol=1e-4, atol=1e-6)

    @parameterized.expand(load_params("kaldi_test_mfcc_args.jsonl"))
    @skipIfNoExec("compute-mfcc-feats")
    def test_mfcc(self, kwargs):
        """mfcc should be numerically compatible with compute-mfcc-feats"""
        wave_file = get_asset_path("kaldi_file.wav")
        waveform = load_wav(wave_file, normalize=False)[0].to(dtype=self.dtype, device=self.device)
        result = torchaudio.compliance.kaldi.mfcc(waveform, **kwargs)
        command = ["compute-mfcc-feats"] + convert_args(**kwargs) + ["scp:-", "ark:-"]
        kaldi_result = run_kaldi(command, "scp", wave_file)
        self.assert_equal(result, expected=kaldi_result, rtol=1e-4, atol=1e-5)

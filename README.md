## OuteTTS Voices Collection

Free Voices for [OuteTTS](https://github.com/edwko/OuteTTS).

## Voices
- en_US Female [listen](https://raw.githubusercontent.com/akhenakh/outetts-voices/main/mp3/en_us_female_speaker.mp3)
- en_US Male [listen](https://raw.githubusercontent.com/akhenakh/outetts-voices/main/mp3/en_us_male_speaker.mp3)
- fr_CAN Female [listen](https://raw.githubusercontent.com/akhenakh/outetts-voices/main/mp3/fr_can_female_speaker.mp3)
- fr_CAN Female 2 [listen](https://raw.githubusercontent.com/akhenakh/outetts-voices/main/mp3/fr_can_female2_speaker.mp3)
- fr_CAN Male [listen](https://raw.githubusercontent.com/akhenakh/outetts-voices/main/mp3/fr_can_male_speaker.mp3)



## Usage

```python
import outetts

# Initialize the interface
interface = outetts.Interface(
    config=outetts.ModelConfig.auto_config(
        model=outetts.Models.VERSION_1_0_SIZE_1B,
        # For llama.cpp backend
        backend=outetts.Backend.LLAMACPP,
        quantization=outetts.LlamaCppQuantization.FP16
        # For transformers backend
        # backend=outetts.Backend.HF,
    )
)


# Load a saved speaker profile
speaker = interface.load_speaker("voices/en_us_female_speaker.json")


output = interface.generate(
    config=outetts.GenerationConfig(
        text="Welcome to Vuta Stream, your local news video streaming platform. We create ultra-specific niche channels just for you. You can request for new channels, and soon even create your own channels.",
        generation_type=outetts.GenerationType.CHUNKED,
        speaker=speaker,
        sampler_config=outetts.SamplerConfig(
            temperature=0.4
        ),
    )
)

# Save to file
output.save("output.wav")

```

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

en_msg = "Welcome to Vuta Stream, your local news video streaming platform. We create ultra-specific niche channels just for you. You can request for new channels, and soon even create your own channels."

fr_msg = "Bienvenue sur Vuta Stream, votre plateforme de streaming vidéo d'actualités locales. Nous créons des chaînes ultra-spécialisées rien que pour vous. Vous pouvez demander de nouvelles chaînes et bientôt créer les vôtres."


for name in ["en_us_female_speaker", "en_us_male_speaker", "fr_can_female_speaker", "fr_can_female2_speaker", "fr_can_male_speaker"]:
    # Load a saved speaker profile
    speaker = interface.load_speaker(f"voices/{name}.json")
    
    # If name starts with "en", use en_msg, otherwise use fr_msg
    if name.startswith("en"):
        msg = en_msg
    else:
        msg = fr_msg
    
    # Generate audio
    output = interface.generate(
        config=outetts.GenerationConfig(
            text=msg,
            generation_type=outetts.GenerationType.CHUNKED,
            speaker=speaker,
            sampler_config=outetts.SamplerConfig(
                temperature=0.4
            ),
        )
    )
    
    # Save to file
    output.save(f"{name}.wav")

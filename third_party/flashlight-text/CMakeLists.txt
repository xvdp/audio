set(
  sources
  submodule/flashlight/lib/text/decoder/Decoder.h
  submodule/flashlight/lib/text/decoder/LexiconDecoder.h
  submodule/flashlight/lib/text/decoder/LexiconDecoder.cpp
  submodule/flashlight/lib/text/decoder/Trie.h
  submodule/flashlight/lib/text/decoder/Trie.cpp
  submodule/flashlight/lib/text/decoder/Utils.h
  submodule/flashlight/lib/text/decoder/Utils.cpp
  submodule/flashlight/lib/text/decoder/lm/KenLM.h
  submodule/flashlight/lib/text/decoder/lm/KenLM.cpp
  submodule/flashlight/lib/text/decoder/lm/ZeroLM.h
  submodule/flashlight/lib/text/decoder/lm/ZeroLM.cpp
  submodule/flashlight/lib/text/decoder/lm/LM.h
  submodule/flashlight/lib/text/dictionary/Dictionary.h
  submodule/flashlight/lib/text/dictionary/Dictionary.cpp
  submodule/flashlight/lib/text/dictionary/Utils.h
  submodule/flashlight/lib/text/dictionary/Utils.cpp
  submodule/flashlight/lib/text/String.h
  submodule/flashlight/lib/text/String.cpp
  )
add_library(flashlight_text STATIC ${sources})
target_include_directories(flashlight_text PUBLIC submodule)
target_link_libraries(flashlight_text kenlm)
target_compile_definitions(flashlight_text FL_TEXT_USE_KENLM)

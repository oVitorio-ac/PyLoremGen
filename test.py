from pylorem.generator.lorem_ipsum import LoremIpsum


lorem_ipsum = LoremIpsum()
resultado = lorem_ipsum.paragraphs(1, size="large")
print(resultado)

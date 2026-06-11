def validarCelular():
    validar = input("Você deseja validar seu celuar?").lower.stip()
    if validar == "sim" or validar == "s":
        print("celular validado com sucesso")
    else:
        print("autorização bloqueada")
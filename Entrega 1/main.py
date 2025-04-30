import scanner

def run_compiler(code_input):
    import ply.yacc as yacc
    import parser as babyduck_parser

    print("--- Scanner Output ---")
    
    scanner.lexer.lineno = 1
    scanner.lexer.input(code_input)
    

    tokens_list = []
    while True:
        tok = scanner.lexer.token()
        if not tok:
            break
        print(f"[{tok.type}] -> {repr(tok.value)} (linea {tok.lineno})")
        tokens_list.append(tok)

    if not tokens_list:
        print("(No se generaron tokens)")

    print("\n--- Parser Output ---")
    try:
        parser = yacc.yacc(module=babyduck_parser, debug=False, write_tables=False)
        result = parser.parse(input=code_input, lexer=scanner.lexer)

        if result is not None:
            print("Resultado del Parseo (AST simplificado):")
            print(result)
        else:
            print("El parseo falló o no produjo resultado (revisar errores de sintaxis arriba).")

    except Exception as e:
        print(f"EXCEPCIÓN INESPERADA DURANTE EL PARSEO: {e}")


if __name__ == "__main__":
    test_cases = [
    # Caso 1: Código correcto
    """program miPrograma;
    var
        x : int;
        y : float;
    main
    {
        x = 10;
        y = 20.5;
        if (x > 0) {
            y = y + 1.0;
        }
    }
    end""",

    # Caso 2: Error Léxico (carácter prohibido '@')
    """program errorLexico;
    var
        x : int;
    main
    {
        x = 10 @;
    }
    end""",

    # Caso 3: Error Sintáctico (falta de ';')
    """program errorSintactico;
    var
        x : int;
    main
    {
        x = 10
    }
    end""",

    # Caso 4: Expresión matemática correcta
    """program expresionCorrecta;
    var
        resultado : int;
    main
    {
        resultado = (5 + 3) * (2 - 1);
    }
    end""",

    # Caso 5: Error Sintáctico (llave faltante)
    """program errorFaltaLlave;
    var
        y : int;
    main
    {
        y = 25;
    end""",

    # Caso 6: Declaraciones múltiples
    """program multiDeclaraciones;
    var
        a : int;
        b : int;
        c : int;
        d : float;
    main
    {
        a = 1;
        b = 2;
        c = a + b;
        d = c * 1.5;
    }
    end""",

    # Caso 7: Error Léxico (número mal formado)
    """program numeroMalFormado;
    var
        num : float;
    main
    {
        num = 10..5;
    }
    end""",
]


    # --- Bucle Principal de Pruebas ---
    for i, case in enumerate(test_cases):
        print(f"\n======================================")
        print(f"===== PROCESANDO CASO DE PRUEBA {i + 1} =====")
        print(f"======================================")
        print("--- Código Fuente ---")
        print(case)
        print("---------------------")
        run_compiler(case) # Ejecuta el compilador para este caso
        print(f"\n===== FIN CASO DE PRUEBA {i + 1} =====")

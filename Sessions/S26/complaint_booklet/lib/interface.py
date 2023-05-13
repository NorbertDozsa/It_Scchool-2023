class CLIMenu:

    def __init__(self, program_name, command_map) -> None:
        self.__command_map = command_map
        self.program_name = program_name

    def show_main(self):
        while True:
            print(f"{self.program_name:=^50}\n")
            for i, cmd in enumerate(self.__command_map.items(), start=1):
                print(f"{i}. {cmd[0]}")
            try:
                user_choice = int(input("Alege un numar din lista de mai sus: "))
            except TypeError:
                print("EROARE: Te rog sa alegi un numar din numere de mai sus!")
            else:
                print(f"Ai ales: {user_choice}")

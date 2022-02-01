import os


class FileCreator:
    def create_main(self, class_dict:dict):
        print(class_dict)
        name = class_dict['class']['name']
        file_name = f'{name}.py'
        path = os.path.join('created_files', file_name)
        with open(path, 'w+') as file:
            string = f'class {name}:\n'
            functions = list(class_dict['class']['functions'])
            
            for function in functions:
                attrs = class_dict['class']['functions'][function]['attrs']
                print(attrs)
                string += f"\tdef {class_dict['class']['functions'][function]['name']}"
                string += f"(self, {self.create_parameters(attrs)}):\n\t\tpass\n\n"

            file.write(string)
    
    def create_parameters(self, params:dict):
        string = ''
        for param in params:
            string += f'{param}:{params[param]}, '

        return string


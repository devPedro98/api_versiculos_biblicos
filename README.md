# api_versiculos_biblicos

API funcional criada com Python utilizando o Framework Django Rest Framework, com segurança JWT(JSON Web Token).

A API contem paginação de 5 versículos por página, e um limite de 10 acessos por minuto.

## Como utilizar a API:

Faça uma requisição do tipo POST no Link https://versiculos-biblicos.herokuapp.com/login/ utilizando as seguintes credenciais: 

{
	"username":"pedro",
	"password":"Pedro@SantosBarrios1"
}

Após o login feito basta copiar o token gerado no campo "access" conforme mostra a imagem
![image](https://user-images.githubusercontent.com/99411247/175166801-bdbad805-0e0c-459e-b547-1e79be09b752.png)

Login feito e token gerado, através da url https://versiculos-biblicos.herokuapp.com/biblia/ você está pronto para fazer às requisições do tipo GET, POST, PUT e DELETE.

Basta copiar o token e colar nas requisições desejadas, segue exemplo com o tipo GET:
![image](https://user-images.githubusercontent.com/99411247/175167045-f69be4cb-5470-4a01-80ee-7a3994f6be27.png)

Para fazer um POST basta informar os campos abaixo



![image](https://user-images.githubusercontent.com/99411247/175167190-6a9e1065-adf8-4d0e-960f-c94015890dad.png)

PUT e DELETE basta informar o ID, exemplo https://versiculos-biblicos.herokuapp.com/biblia/17/

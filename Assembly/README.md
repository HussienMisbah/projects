this code will take an input message and will start encrypt it with following table :

````
a b c d e f g h i j k l m n o p q r s t u v w x y z

q w e r t y u i o p a s d f g h j k l z x c v b n m 
````
then will decrypt it again.

decryption is in 2 steps :

```
q w e r t y u i o p a s d f g h j k l z x c v b n m 

k x v m c n o p h q r s z y i j a d l e g w b u f t 
```

then the output will be compared to :

```
k x v m c n o p h q r s z y i j a d l e g w b u f t 

a b c d e f g h i j k l m n o p q r s t u v w x y z
```

ex : 

```
input : cat 
encryptyion       : c-> e , a -> q , t -> z  "eqz"
decryption-step 1 : e-> v , q -> k , z -> e  "vke"
decryption-step 2 : v-> c , k -> a , e -> t  "cat"

```

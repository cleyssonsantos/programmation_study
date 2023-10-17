(ns teste.aula5)

(def lista1 [1, 2, 3, 4, 5])
(println lista1)

; Apenas praticando o laço "for"
(def nova-lista (map #(* 2 %) lista1))
(println nova-lista)

(def estoque {"Mochila" 10, "Camiseta" 5}) ; Array Map
(println (class estoque))

(println "Temos" (count estoque) "valores.")
(println "As chaves são" (keys estoque))
(println "Os valores são" (vals estoque))

; Não é comum usar str como chave do Array Map.

(def estoque-novo {:mochila 10
                   :camiseta 5})

(println (assoc estoque :cadeira 3))

(println (update estoque-novo :mochila inc))

(println (dissoc estoque-novo :mochila))
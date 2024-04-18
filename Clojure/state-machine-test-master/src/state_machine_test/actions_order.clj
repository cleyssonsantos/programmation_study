(ns state-machine-test.actions-order
  (:require [tilakone.core :as tk :refer [_]]))

(def signals
  [:S0 :S1 :S2 :S3])

(def estados
  [{::tk/name :start
    ::tk/desc "Estado inicial."
    ::tk/transitions [{::tk/on :S0
                       ::tk/to :validate-credit-card
                       ::tk/actions [:print-start-message]}]}

   {::tk/name :validate-credit-card
    ::tk/desc "Verifica se o limite está disponível."
    ::tk/transitions [{::tk/on :S1
                       ::tk/to :check-limit
                       ::tk/guards [:t1]
                       ::tk/actions [:print-start-message :t1]}]
    ::tk/enter {::tk/guards [:enter1]
                ::tk/actions [:enter1]}
    ::tk/leave {::tk/guards [:leave1]
                ::tk/actions [:leave1]}}

   {::tk/name :check-limit
    ::tk/desc "Verifica se o limite está disponível."
    ::tk/transitions [{::tk/on :S2
                       ::tk/to :final-report
                       ::tk/guards [:t2]
                       ::tk/actions [:print-start-message :t2]}]
    ::tk/enter {::tk/guards [:enter2]
                ::tk/actions [:enter2]}
    ::tk/leave {::tk/guards [:leave2]
                ::tk/actions [:leave2]}}

   {::tk/name :final-report
    ::tk/desc "Realiza o report final."
    ::tk/transitions [{::tk/on _
                       ::tk/actions [:print-start-message]}]}

   {::tk/name :error
    ::tk/desc "Valida as informações passadas pelo cliente."
    ::tk/transitions [{::tk/on _
                       ::tk/actions [:print-start-message]}]}])


(defmulti actions (fn [signal fsm]
                    signal))


(defmethod actions :default
  [action fsm]
  (let [signal (get-in fsm [::tk/signal])]
    (println (format "ACTION %s - SIGNAL %s" action  signal)))
  fsm)

(defmethod actions :print-start-message
  [action fsm]
  (let [signals-index (.indexOf signals (get-in fsm [::tk/signal]))
        process-name (get-in fsm [::tk/process ::tk/states signals-index ::tk/name])
        signal-name (name (get-in fsm [::tk/signal]))]
    (println (str "Iniciando ação: " process-name " - Sinal: " signal-name)))
  fsm)

(defmulti guardian (fn [guard fsm]
                     guard))

(defmethod guardian :default
  [guard fsm]
  (let [signal (get-in fsm [::tk/signal])]
    (println (format "GUARD %s - SIGNAL %s"  guard  signal)))
  true)


(defn test-order
  "Máquina de estado simples com objetivo de testar a ordem de ações/guardians
  e em quais momentos os signals são trocados"
  []
  (let [process {::tk/states  estados
                 ::tk/state   :start
                 ::tk/action! (fn [{::tk/keys [signal action] :as fsm}] ;; Usando o valor :action para definir quais actions chamar
                                (actions action fsm))
                 ::tk/guard?  (fn [{::tk/keys [signal guard] :as fsm}] ;; Usando o signal para definir qual guardian chamar
                                (guardian guard fsm))}
        result (reduce tk/apply-signal process signals)
        report (get-in result [:S3])]
    report))



(comment
  (test-order))


(defn continue-from-state
  "Continua a execução da máquina a partir de um estado específico."
  [estado-inicial sinal]
  (let [processo-inicial {::tk/states estados
                          ::tk/state estado-inicial
                          ::tk/action! (fn [{::tk/keys [sinal action] :as fsm}]
                                         (actions action fsm))
                          ::tk/guard?  (fn [{::tk/keys [sinal guard] :as fsm}]
                                         (guardian guard fsm))}
        sinais-restantes (drop-while #(not= % sinal) signals)
        resultado-final (loop [acc processo-inicial remaining-signals sinais-restantes]
                          (if (or (and (nil? (tk/transfers-to acc sinal))
                                       (empty? remaining-signals))
                                  (empty? remaining-signals))
                            acc ;; acumulator
                            (let [primeiro-sinal-da-lista (first remaining-signals)
                                  result (tk/apply-signal acc primeiro-sinal-da-lista)]
                              (recur result (rest remaining-signals)))))]
    resultado-final))

(println (tk/transfers-to {::tk/states estados
                           ::tk/state :validate-credit-card
                           ::tk/action! (fn [{::tk/keys [sinal action] :as fsm}]
                                          (actions action fsm))
                           ::tk/guard?  (fn [{::tk/keys [sinal guard] :as fsm}]
                                          (guardian guard fsm))} :S1))

(continue-from-state :validate-credit-card :S1)

(comment
 (continue-from-state :validate-credit-card :S1))





(defn lr
  [x level result]
  (if (< level 2)
    result
    (recur x (dec level) (conj result [level x]))))


(defn lb
  [x level count]
  (if (< level 2)
    count
    (do
      (println level count)
      (recur x (dec level) (* x count)))))


(defn lr2
  [x result]
  (let [[target] (filter (fn [v] (and (= (:color v) "r") (> (:level v) 1))) result)]
    (if (= target nil)
      result
      (recur x (concat (remove (fn [v] (= v target)) result) [{:color "b" :level (:level target) :count x}
                                                              {:color "r" :level (dec (:level target))}])))))


(defn lb2
  [x result]
  (let [[target] (filter (fn [v] (and (= (:color v) "b") (> (:level v) 1))) result)]
    (if (= target nil)
      result
      (recur x (concat (remove (fn [v] (= v target)) result) [{:color "b" :level (dec (:level target)) :count (* (:count target) x)}
                                                              {:color "r" :level (dec (:level target))}])))))


(concat [] [{1 2} {1 3}])


(defn l
  [x y result]
  (let [r (lb2 y (lr2 x result))
        [target] (filter (fn [v] (and (= (:color v) "r") (> (:level v) 1))) r)]
    (println r)
    (if (= target nil)
      r
      (recur x y r))))


(reduce (fn [acm v]
          (if (= (:color v) "b")
            (+ acm (:count v))
            acm)) 0 (l 5 5 [{:color "r" :level 10}]))


;; => 15258725
;;     9765625

(lr2 3 [{:color "r" :level 3}])


(lb2 4 (lr2 3 [{:color "r" :level 2}]))


;; => ({:color "b", :level 3, :count 3}
;;     {:color "b", :level 2, :count 3}
;;     {:color "r", :level 1})

(mapv println (lb2 5 (lr2 5 [{:color "r" :level 10}])))


;; => ({:color "r", :level 1}
;;     {:color "r", :level 2}
;;     {:color "b", :level 1, :count 6}
;;     {:color "r", :level 1}
;;     {:color "b", :level 1, :count 12}
;;     {:color "r", :level 1})

;; => ({:color "b", :level 10}
;;     {:color "b", :level 9}
;;     {:color "b", :level 8}
;;     {:color "b", :level 7}
;;     {:color "b", :level 6}
;;     {:color "b", :level 5}
;;     {:color "b", :level 4}
;;     {:color "b", :level 3}
;;     {:color "b", :level 2}
;;     {:color "r", :level 1})

(remove (fn [v] (= v target)))


;; 再帰なんだけど、使い回しがおおいのでそれをくふうしないといけない。


[{:color "b" :level 2} {:color "r" :level 1}]

(map (fn [[l c]] (lb 4 l c)) (lr 3 2 []))

(map (fn [[l c]] (lb 4 l c)) (lr 5 1 []))

(lb 3 4 1)

(reduce (fn [acm [l c]] (+ acm (lb 5 l c))) 0 (lr 5 10 []))
(map (fn [[l c]] (lb 5 l c)) (lr 5 10 []))

(map (fn [[l c]] (lb 4 l c)) (lr 3 2 []))
2 3 4


(let [[n x y] (read-line)])


;; levelを一つ減らすたびに個数が増えるのでべき乗の構造をもってるぞ
;; そうするとあの速度アップの方法も使えるのか。

;; [3 1] => [2 3]
;; [2 3] => [1 3] * 3
;; 

;; [4 1] => [3 3]
;; [3 3] => [2 3 * 3]
;; [2 3 * 3] => [1 3 * 3 * 3]
;;

;; そうかそう単純じゃないな。さがった赤のことも考慮しないといけない。
;; ひとつひとつは簡単な気がするけどアウトだな。




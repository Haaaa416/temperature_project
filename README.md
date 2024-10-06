# temperature_project
ppt:有四個ppt儲資料/照片
1. 8/28 https://www.canva.com/design/DAGPDKQ3DmI/XreFMk6gREcnUnsxqg6b3Q/edit?utm_content=DAGPDKQ3DmI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
2. CzFz https://www.canva.com/design/DAGQ1h-LDFQ/W9S_WKW12dlXptqTVN_xNg/edit?utm_content=DAGQ1h-LDFQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
3. 6特徵 https://www.canva.com/design/DAGRqdo8wUc/LLxTiztNXwKbUJlX5oVrRg/edit?utm_content=DAGRqdo8wUc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
4. 5個人 6features https://www.canva.com/design/DAGSVyjv-4A/vwIfcHd2Nwg_XESYIQve9g/edit?utm_content=DAGSVyjv-4A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

1. 8/28中  
   (1)隨機20次訓練中，以三個狀態，兩個特徵(alpha gamma)進行邏輯思迴歸訓練  
      => train : rong 、 yxy ; test : OJH 、 xubo ; validation : kingcloser
         在 Cz 電極位下此種組合 驗證的準確率最高
      => 算出的權重訓練 : 不論是在 "Cz or Fz"電極位下，gamman 所佔的權重比 alpha 都較高 
   (2)原數據是以三個狀態兩個特徵去使用，後來根據文獻告知theta頻帶在疼痛時會被誘發出來，因此增加這個特徵出來  
      => 三個狀態(恆溫舒服 升溫舒服 升溫不舒服) 三個特徵  
   (3)經過資料清理(以下是資料清理步驟):  
      ![image](https://github.com/user-attachments/assets/ff23ca12-9bd4-442f-9422-42ba13365adf)  
      I 最後使用四分位距擷取特徵資料  
      II 恆溫舒服&升溫舒服:theta & alpha 取 Q1-Q3;gamma 取 最小值到中位數  
      III 升溫不舒服:theta & alpha 取 Q1-Q3;gamma 取中位數到最大值  
   (4)以四個模型進行訓練:邏輯迴歸、隨機森林、SVM、決策樹  
      ![image](https://github.com/user-attachments/assets/333b4b23-bb43-49fa-bb0d-9e5eb9404446)
      ![image](https://github.com/user-attachments/assets/fe393a13-7e81-4697-96d6-3b093e0056d8)  
      => 根據第一張圖:不論在哪個電極位上(Cz or Fz)，以三個特徵進行訓練效過最佳  
      => 根據第二章圖:不論在哪個電極位上(Cz or Fz)，以三個特徵進行訓練效過最佳  
   (5)經由四分位距畫出的盒方圖發現在這兩個狀態(恆溫舒服、升溫舒服)，分不出太大差異  
      => 同時這兩個階段實驗，受試者皆感受到"舒服"  
      ![image](https://github.com/user-attachments/assets/85623a3d-e489-4db7-ac74-73808ab1abfb)  
      => 因此改成兩種狀態去訓練 : 舒服 & 不舒服  
   (6)以四個模型進行訓練:邏輯迴歸、隨機森林、SVM、決策樹  
      ![image](https://github.com/user-attachments/assets/7307b540-2ef3-4a18-8271-7a4ed79afa52)
      ![image](https://github.com/user-attachments/assets/a201dfb4-8275-4ff0-be92-53afb21aa233)  
      => 根據第一張圖:只要有 "gamma" 頻帶特徵，準確率都能高達1.0  
      => 根據第二章圖:整體來說 "Cz" 電極位訓練效果優於 "Fz" ; 除了羅吉斯迴歸以外，其餘效果皆達到1.0
   (7)總結: "gamma" 特徵很顯卓
2.CzFz中  
  (1)以2個狀態、3個特徵進行訓練、train : rong 、 yxy ; test : OJH 、 xubo ; validation : kingcloser  
     不過此驗證資料有兩種(第一階段溫感實驗;第二階段溫感實驗)  
     ![image](https://github.com/user-attachments/assets/694b4db4-eb05-4e48-8160-a15c924e7754)  
     => 在訓練集準確率下，隨機森林、決策樹訓練效果皆是最好的  
     => 在驗證集準確率下，隨機森林、決策樹訓練驗證出來不相上下(不論哪階段實驗)  
     => 所有模型在驗證集下，都有一個共通點， " Fz " 電極位訓練效果大多是最差的，不論哪階段實驗，唯獨在 SVM 第一階段實驗中高於 "Cz&Fz"電極位
   (2)因此去看驗證集在不同階段溫感實驗中不舒服狀態下混淆矩陣預測的準確率
      ![image](https://github.com/user-attachments/assets/4912ebc2-5e0a-4982-b98f-d6aa5205e1ca)  
      I 第一階段實驗  
        => Fz在第一階段實驗中預測的準確率最低  
        => 隨機森林在三個電位下準確率都最高(除cz&fz)  
      II 第二階段實驗  
         => Fz在第一階段實驗中預測的準確率最低  
         => 隨機森林在三個電位下準確率都最高  
   (3)總結:由此可見大部分下在哪一階段溫感實驗隨機森林訓練效果都較佳、Fz的準確率最低  
      *討論隨機森林與決策樹前提下:由於原模型(訓練模型)是第一階段溫感實驗，並不能表示拿第二階段溫感實驗就不準確  
3.6特徵  
   (1)以2個狀態、6個特徵進行訓練、train : rong 、 yxy ; test : OJH 、 xubo ; validation : kingcloser  
      => 從前面訓練結果得到 "gamma"特徵很顯卓，但是gamma頻帶很多段，在前面訓練都是以(70-90Hz)，所以再來改成每10Hz訓練，分為:  
      ![image](https://github.com/user-attachments/assets/a7256197-802c-4a70-9b84-7d086eb0bf96)  
   (2)從盒方圖看出在第一階段實驗的驗證集，出現其他受試者沒有出現的現象:兩個狀態下幾乎分不出差異  
      => 因此我才增加第二階段實驗的驗證集的訓練  
      => 能明顯展示出差異，因此推斷第二階段實驗是更精準的實驗  
   (3)![image](https://github.com/user-attachments/assets/6b946856-6cb3-41ef-90d9-81b66fc77065)  
      => 隨機森林測試準確率是最好;驗證集準確率在第一間段實驗則是SVM最好、第二間段實驗則是邏輯回歸最好  
      => 但四種模型下大部分驗證集在第二階段溫感實驗的準確率優於第一階段實驗
      => 由此可知第二階段實驗的準確率會比第一階段更好，更精準實驗(紅外線實驗穩定性較高)
      => 此訓練方式並非使用5個人數據放一起去分配驗證集、測試集比例，因此會造成第一階段實驗驗證準確率較低，  
         從盒方圖可以看出來訓練集、測試集資料分布很像，但是驗證集卻是偏差，所以導致第一階段實驗驗證準確率較低
   (4)因此去看驗證集在不同階段溫感實驗中不舒服狀態下混淆矩陣預測的準確率
      ![image](https://github.com/user-attachments/assets/49e2e594-0153-4690-8483-c767dfe272c4)  
      I 第一階段實驗  
        => Fz在第一階段實驗中驗證集的準確率最低  
        => 隨機森林在三個電位下準確率都最高(除cz&fz)  
      II 第二階段實驗
         => cz & fz 、fz 在第二階段實驗中驗證集的準確率最低
         => 邏輯回歸在三個電位下準確率都最高
   (5)總結:由此可見大部分下在哪一階段溫感實驗隨機森林、羅吉斯回歸效果都較佳、Fz的準確率最低
4.5個人
   (1)

   


 
    


      





# temperature_project
ppt:有四個ppt儲資料/照片
1. 8/28 https://www.canva.com/design/DAGPDKQ3DmI/XreFMk6gREcnUnsxqg6b3Q/edit?utm_content=DAGPDKQ3DmI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
2. CzFz https://www.canva.com/design/DAGQ1h-LDFQ/W9S_WKW12dlXptqTVN_xNg/edit?utm_content=DAGQ1h-LDFQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
3. 6特徵 https://www.canva.com/design/DAGRqdo8wUc/LLxTiztNXwKbUJlX5oVrRg/edit?utm_content=DAGRqdo8wUc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
4. 5個人 6features https://www.canva.com/design/DAGSVyjv-4A/vwIfcHd2Nwg_XESYIQve9g/edit?utm_content=DAGSVyjv-4A&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

1. 8/28中
   (1)原數據是以三個狀態兩個特徵去使用，後來根據文獻告知theta頻帶在疼痛時會被誘發出來，因此增加這個特徵出來  
      => 三個狀態(恆溫舒服 升溫舒服 升溫不舒服) 三個特徵  
   (2)經過資料清理(以下是資料清理步驟):  
      ![image](https://github.com/user-attachments/assets/ff23ca12-9bd4-442f-9422-42ba13365adf)  
      最後使用四分位距擷取特徵資料  
      恆溫舒服&升溫舒服:theta & alpha 取 Q1-Q3  
                      gamma 取 最小值到中位數  
      升溫不舒服:theta & alpha 取 Q1-Q3  
                gamma 取中位數到最大值  
   (3)以四個模型進行訓練:邏輯迴歸、隨機森林、SVM、決策樹  
      ![image](https://github.com/user-attachments/assets/333b4b23-bb43-49fa-bb0d-9e5eb9404446)  
      ![image](https://github.com/user-attachments/assets/fe393a13-7e81-4697-96d6-3b093e0056d8)  
      => 根據第一張圖:不論在哪個電極位上(Cz or Fz)，以三個特徵進行訓練效過最佳  
      => 根據第二章圖:不論在哪個電極位上(Cz or Fz)，以三個特徵進行訓練效過最佳  



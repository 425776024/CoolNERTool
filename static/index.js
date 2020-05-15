document.onkeydown=function(event){
    var e = event || window.event || arguments.callee.caller.arguments[0];
    let sel = document.getSelection();
    select_ele=sel.anchorNode.parentElement;
    select_txt_id=select_ele['id'];
    if (key_code==32){
        save_button_func();
        return;
    }

    if (select_txt_id == "text"){
        ele_start=sel.anchorOffset
        ele_end=sel.extentOffset
        start=Math.min(ele_start,ele_end)
        end=Math.max(ele_start,ele_end) -1
        dell_selected(e && e.keyCode,start,end)
    }
};


function dell_selected(code,start,end){
    //0:48  1:49    2:50    3:51    4:52
    if (code in key_code){
        HEAD_TAG=key_code[code][0];
        INNER_TAG=key_code[code][0];
    }
    for (var i=start;i<=end;i++){
        if (i==start){
            labeling_dict[i]=HEAD_TAG
        }else{
            labeling_dict[i]=INNER_TAG
        }
    }
    flush();
}

function flush(){
    show_html_text=construct_show_text();
    elem=document.getElementById("show");
    re_show_text(elem,show_html_text);
}
function getSelectText () {
    return window.getSelection ? window.getSelection().toString() :
    document.selection.createRange().text;
}

function getSelect() {
    let select = document.getSelection();
    return select;
}

function construct_show_text(){
//根据labeling_dict重构显示
    tp_show_html_text="";
    for (var i=0;i<text.length;i++){
        p_txt=text[i];
        p_tag=labeling_dict[i];
        p_color=color_map[p_tag];
        p=construct_elem_p(p_txt,p_color);
        tp_show_html_text=tp_show_html_text+p;
    }
    return tp_show_html_text;
}

function construct_elem_p(text,color){
    s="<p style=\"color:"+color+"\">"+text+"</p>";
    return s;
}



function re_show_text(elem,html_text){
    elem.innerHTML=html_text;
}

function save_button_func(){
//根据labeling_dict构造提交文本
    tp_lab_text=''
    for (var i=0;i<text.length;i++){
        if (i in labeling_dict){
            tp_lab_text=tp_lab_text+labeling_dict[i]
        }else{
            if(i<text.length-1){
                tp_lab_text=tp_lab_text+"O"
            }
        }
        if(i<text.length-1){
            tp_lab_text=tp_lab_text+" "
        }
    }
    cur_idx=document.getElementById("cur_idx").innerText;
    post('/submit_labling',{"lab_text":tp_lab_text,'token_size':text.length,'cur_idx':cur_idx})
}

function post(URL, PARAMS) {
  //  post('pages/statisticsJsp/excel.action',{html:prnhtml,cm1:'sdsddsd',cm2:'haha'});
  var temp = document.createElement("form");
  temp.action = URL;
  temp.method = "post";
  temp.style.display = "none";
  for (var x in PARAMS) {
    var opt = document.createElement("textarea");
    opt.name = x;
    opt.value = PARAMS[x];
    // alert(opt.name)
    temp.appendChild(opt);
  }
  document.body.appendChild(temp);
  temp.submit();
  return temp;
}

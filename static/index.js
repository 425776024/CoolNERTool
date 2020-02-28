

labeling_dict=[]
//标注文本
text=''
//富文本显示构造文本


color_map={"O":"black",
            "B-P":"#0000FF","I-P":"#00CCFF",
            "B-ORG":"#00FF33","I-ORG":"#009933",
            "B-LOC":"#660099","I-LOC":"#666699",
            "B-COM":"red","I-COM":"#CC3300"
            }


window.onload = function(){

    text=document.getElementById("text").innerText;
    label_sen_txt=document.getElementById("label_sen").innerText;

    labeling_dict=label_sen_txt.split(' ')
    console.log(labeling_dict);
    flush();
    console.log(text[0])
    console.log(text)
    console.log(text.length)
    console.log(text[text.length-1])

}

document.onkeydown=function(event){
    var e = event || window.event || arguments.callee.caller.arguments[0];
    sel=getSelect();

    select_ele=sel.anchorNode.parentElement;
    select_txt_id=select_ele['id'];
    if (select_txt_id == "text"){

        console.log(e.keyCode+':'+getSelectText());
        console.log(sel);

        ele_start=sel.anchorOffset
        ele_end=sel.extentOffset
        start=Math.min(ele_start,ele_end)
        end=Math.max(ele_start,ele_end) -1

        console.log(text[start]+'-'+text[end])
        dell_selected(e && e.keyCode,start,end)
    }
};


function dell_selected(code,start,end){
    //0:48  1:49    2:50    3:51    4:52
    console.log(start+'-'+end)
    TAG="O"
    if (code==48){
        HEAD_TAG="O"
        INNER_TAG="O"
    }
    if (code==49){
        HEAD_TAG="B-P"
        INNER_TAG="I-P"
    }
    if (code==50){
        HEAD_TAG="B-ORG"
        INNER_TAG="I-ORG"
    }
    if (code==51){
        HEAD_TAG="B-LOC"
        INNER_TAG="I-LOC"
    }
    if (code==52){
        HEAD_TAG="B-COM"
        INNER_TAG="I-COM"
    }
    console.log(HEAD_TAG+":"+INNER_TAG)
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

function back_button_func(){
    cur_idx=document.getElementById("cur_idx").innerText;
    cur_idx=parseInt(cur_idx);
    next_idx=cur_idx+1;
    host = window.location.host;
    url='http://'+host+'/labeling/'+next_idx;
    console.log(url)
    window.location.href = url;
}

function pre_button_func(){
    cur_idx=document.getElementById("cur_idx").innerText;
    cur_idx=parseInt(cur_idx);
    next_idx=cur_idx-1;
    if (next_idx<0){
        next_idx=0;
    }
    host = window.location.host;
    url='http://'+host+'/labeling/'+next_idx;
    console.log(url)
    window.location.href = url;
}
function save_button_func(){
//根据labeling_dict构造提交文本
    console.log(labeling_dict)
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
    console.log(cur_idx+':'+tp_lab_text);
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

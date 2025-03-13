select
	v.id_voluntar, tv.id_task, t.id_proiect
from voluntari v
join task_voluntar tv on tv.id_voluntar =v.id_voluntar
join task_uri t on t.id_task = tv.id_task
where v.id_voluntar >12 and t.id_proiect >3;

select
    v.id_voluntar,
    v.nume,
    count(tv.id_asoc)as numar_task_uri
from voluntari v
join task_voluntar tv on v.id_voluntar = tv.id_voluntar
group by v.id_voluntar, v.nume
having count(tv.id_asoc) > 1;


select * from task_voluntar;
    
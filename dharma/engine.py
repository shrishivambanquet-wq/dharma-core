from .packets import DAP
from .validator import validate
from .lvp import verify
from .constraints import check
from .evidence import record

class DharmaEngine:

    def __init__(self):
        self.ledger={}
        self.evidence=[]

    def grant(self,issuer,subject,authority,constraints):

        packet=DAP(
            issuer=issuer,
            subject=subject,
            authority=authority,
            constraints=constraints
        )

        validate(packet)

        self.ledger[packet.packet_id]=packet

        return packet

    def delegate(self,parent_id,subject,constraints=None):

        parent=self.ledger[parent_id]

        verify(parent,self.ledger)

        new_constraints=dict(parent.constraints)

        if constraints:
            new_constraints.update(constraints)

        packet=DAP(
            issuer=parent.subject,
            subject=subject,
            authority=parent.authority,
            constraints=new_constraints,
            parent_id=parent.packet_id
        )

        validate(packet)

        self.ledger[packet.packet_id]=packet

        return packet

    def execute(self,packet_id,request):

        packet=self.ledger[packet_id]

        verify(packet,self.ledger)

        check(packet,request)

        ev=record(packet,request,"PASS")

        self.evidence.append(ev)

        return ev

    def revoke(self,packet_id):

        self.ledger[packet_id].revoked=True

        return {"status":"REVOKED","packet":packet_id}

    def lookup(self,packet_id):

        return self.ledger[packet_id]
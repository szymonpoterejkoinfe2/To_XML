
class DocSpec:
    def __init__(this, DocRefId,DocTypeIndic):
        this.DocRefId = DocRefId
        this.DocTypeIndic = DocTypeIndic

    def presentDocSpec(this):
        print(f"my DocRefId is {this.DocRefId} and DocTypeIndic is {this.DocTypeIndic}")
        
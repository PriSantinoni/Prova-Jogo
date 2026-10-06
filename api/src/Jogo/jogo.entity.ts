import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity('jogo')
export class Jogo {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ length: 120 })
  nome: string;

  @Column({ length: 120})
  plan: string;

  @Column({ type: 'text', nullable: true })
  start_date: date;
}

import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Produto } from './produto.entity';
import { JogoController } from './jogo.controller';
import { JogoService } from './jogo.service';

@Module({
  imports: [TypeOrmModule.forFeature([Produto])],
  controllers: [JogoController],
  providers: [JogoService],
})
export class JogoModule {}
